$(document).ready(function() {
    let input_message = $('#input-message');
    let message_body = $('.msg_card_body');
    let send_message_form = $('#send-message-form');
    const USER_ID = $('#logged-in-user').val();
    let socket;

    function getWebSocketEndpoint(thread_id) {
        let loc = window.location;
        let wsStart = 'ws://';
        if (loc.protocol === 'https:') {
            wsStart = 'wss://';
        }
        return wsStart + loc.host + "/chat/" + thread_id + "/";
    }

    function openSocket(thread_id) {
        if (socket) {
            socket.close();
        }
        socket = new WebSocket(getWebSocketEndpoint(thread_id));

        socket.onopen = function(e) {
            console.log('open', e);
            send_message_form.on('submit', function(e) {
                e.preventDefault();
                let message = input_message.val();
                let send_to = get_active_other_user_id();
                let thread_id = get_active_thread_id();

                let data = {
                    'message': message,
                    'sent_by': USER_ID,
                    'send_to': send_to,
                    'thread_id': thread_id
                };
                data = JSON.stringify(data);
                socket.send(data);
                $(this)[0].reset();
            });
        };

        socket.onmessage = function(e) {
            console.log('message', e);
            let data = JSON.parse(e.data);
            let message = data['message'];
            let sent_by_id = data['sent_by'];
            let thread_id = data['thread_id'];
            newMessage(message, sent_by_id, thread_id);
        };

        socket.onerror = function(e) {
            console.log('error', e);
        };

        socket.onclose = function(e) {
            console.log('close', e);
        };
    }

    function newMessage(message, sent_by_id, thread_id) {
        if ($.trim(message) === '') {
            return false;
        }
        let message_element;
        let chat_id = 'chat_' + thread_id;
        let timestamp = getCurrentTime(); // Get current time dynamically

        if (sent_by_id == USER_ID) {
            message_element = `
                <div class="d-flex mb-4 replied">
                    <div class="msg_cotainer_send">
                        ${message}
                        <span class="msg_time_send">${timestamp}</span>
                    </div>
                    <div class="img_cont_msg">
                        <img src="/static/img/person.svg" class="rounded-circle user_img_msg" alt="people" width="132" height="26">
                    </div>
                </div>
            `;
        } else {
            message_element = `
                <div class="d-flex mb-4 received">
                    <div class="img_cont_msg">
                        <img src="/static/img/person-other.svg" class="rounded-circle user_img_msg" alt="people" width="132" height="26">
                    </div>
                    <div class="msg_cotainer">
                        ${message}
                        <span class="msg_time">${timestamp}</span>
                    </div>
                </div>
            `;
        }

        let message_body = $(`.messages-wrapper[chat-id="${chat_id}"] .msg_card_body`);
        message_body.append($(message_element));
        message_body.animate({
            scrollTop: $(document).height()
        }, 100);
        input_message.val(null);
    }

    function getCurrentTime() {
        let now = new Date();
        let date = now.getDate().toString().padStart(2, '0');
        
        // Array of day names, Sunday is 0, Monday is 1, etc.
        const dayNames = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
        let day = dayNames[now.getDay()];

        let hours = now.getHours();
        let minutes = now.getMinutes().toString().padStart(2, '0');

        // Convert 24-hour format to 12-hour format with leading zero
        hours = hours.toString().padStart(2, '0'); // Ensure hours are two digits

        return `${date} ${day}, ${hours}:${minutes}`;
    }

    $('.contact-li').on('click', function() {
        let thread_id = $(this).attr('chat-id').replace('chat_', '');
        updateChat(thread_id);
    });

    function updateChat(thread_id) {
        if (thread_id) {
            // Show chat content and hide default message
            $('.default-message').removeClass('is_active');
            $('.chat-content').addClass('is_active');
            openSocket(thread_id);
        } else {
            // Show default message and hide chat content
            $('.default-message').addClass('is_active');
            $('.chat-content').removeClass('is_active');
            if (socket) {
                socket.close();
            }
        }
    }

    // On page load, check if there is an active thread
    let current_path = window.location.pathname;
    let thread_id = null;

    // Example: If URL path is /chat/123/ -> Extract thread ID 123
    let match = current_path.match(/^\/chat\/(\d+)\/$/);
    if (match) {
        thread_id = match[1];
    }

    updateChat(thread_id);

    // Handle form submission
    send_message_form.on('submit', function(e) {
        e.preventDefault();
        let message = input_message.val();
        let send_to = get_active_other_user_id();
        let thread_id = get_active_thread_id();

        let data = {
            'message': message,
            'sent_by': USER_ID,
            'send_to': send_to,
            'thread_id': thread_id
        };
        data = JSON.stringify(data);
        socket.send(data);
        $(this)[0].reset();
    });

    function get_active_other_user_id() {
        let other_user_id = $('.messages-wrapper.is_active').attr('other-user-id');
        other_user_id = $.trim(other_user_id);
        return other_user_id;
    }

    function get_active_thread_id() {
        let chat_id = $('.messages-wrapper.is_active').attr('chat-id');
        let thread_id = chat_id.replace('chat_', '');
        return thread_id;
    }
});
