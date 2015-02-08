/**
 * Created by 001350 on 2015/2/5.
 */

$(function () {
        $('#login_form').validate({
            onKeyup: true,
            eachValidField: function () {
                $(this).closest('div').removeClass('has-error').addClass('has-success');
            },
            eachInvalidField: function () {
                $(this).closest('div').removeClass('has-success').addClass('has-error');
            }
        });

        $('#login_form').on('submit', function() {
            $(this).ajaxSubmit({
                type: 'post',
                url: 'login/',
                dataType: "json",
                success: function(data) {
                    //TODO
                    //if(data.success) {
                        window.location = 'my_home'
                    //}
                },
                error: function(data) {
                    alert(data);
                }
            });
            return false;
        });



    }
)