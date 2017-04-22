/**
 * Created by arran on 19/04/17.
 */

$(function () {
    $('a.post-like').on('click', function (e) {
        e.preventDefault();
        var $this = $(this);

        $.ajax({
            url: '/blog/ajax/post-like/',
            type: 'POST',
            data: {id: $(this).data('id')},

            // handle a successful response
            success: function (data) {
                if (data['status'] === 'ok') {
                    if (data['liked']) {
                        $this.find('span.glyphicon').removeClass('glyphicon-heart-empty').addClass('glyphicon-heart')
                        triggerMessage('success', 'Yay')
                    } else {
                        $this.find('span.glyphicon').removeClass('glyphicon-heart').addClass('glyphicon-heart-empty')
                    }
                } else {
                    triggerMessage('There was an error. Please try again later.', 'error');
                }
            },
            // handle a non-successful response
            error: function(xhr, errmsg, err){
                triggerMessage('There was an error. Please try again later.', 'error');
                console.log(xhr.status + ": " + xhr.responseText);
            }
        })
    })
});