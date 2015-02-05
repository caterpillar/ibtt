/**
 * Created by 001350 on 2015/2/5.
 */

$(function () {
        $('#login_form').validate({
            onKeyup: true,
            focusCleanup: true, focusInvalid: false,
            errorClass: "unchecked",
            validClass: "checked",
            errorElement: "span",
            eachValidField: function () {
                $(this).closest('div').removeClass('has-error').addClass('has-success');
            },
            eachInvalidField: function () {
                $(this).closest('div').removeClass('has-success').addClass('has-error');
            },
            submitHandler: function (form) {
                alert(1);
            }
        });

        $('#login_form').on('submit', function() {
            $(this).ajaxSubmit({
                type: 'post',
                url: 'login',
                dataType: "json",
                success: function(data) {
                    alert(data);
                },
                error: function(data) {
                    alert(data);
                }
            });
            return false;
        });



    }
)