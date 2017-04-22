/**
 * Created by arran on 20/04/17.
 */

function triggerMessage(status, message) {
    var $messageContainer = $('#messages-container');
    var $messages = $messageContainer.find('.alert');

    // Remove any messages that are already on screen
    if ($messages.length) {
        $messages.each(function () {
            var $this = $(this);
            $this.animate({'top': '-200px'}, 500, function ($this) {
                $this.remove()
            });
        })
    }

    // Create the message element and close icon
    var $messageAlert = $('<div class="alert alert-dismissable"></div>')
        .addClass('alert-' + status)
        .text(message);
    var $messageClose = $('<a href="#" class="close" aria-label="close">&times;</a>');

    // Add the element to the message container and animate it into view
    $messageContainer.append($messageAlert.append($messageClose));
    $messageAlert.animate({'top':'90px'}, 500);

    // Remove the message after 4 seconds
    setTimeout(function(){
        $messageAlert.animate({'top': '-200px'}, 500, function () {
            $messageAlert.remove()
        })
    }, 4000);
}

$(function() {
    var $messagesContainer = $('#messages-container');
    var $messages = $messagesContainer.find('.alert');

    // Display any messages have been added to the template context on page load
    if ($messages.length) {
        var top = 90;

        $messages.each(function () {
            var $this = $(this);
            $this.animate({'top': top}, 500);

            // If there are multiple messages then display stack them underneath each other
            top += 61;

            // Remove the message after 4 seconds
            setTimeout(function(){
                $this.animate({'top': '-200px'}, 500, function () {
                    $this.remove()
                })
            }, 4000);
        })
    }

    // Allow the user to close the message
    $messagesContainer.on('click', '.close', function(e) {
        e.preventDefault();

        var $message = $(this).parent();
        $message.remove()
    })
});