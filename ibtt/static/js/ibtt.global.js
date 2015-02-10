/**
 * Created by 001350 on 2015/2/10.
 */

$(function () {
    $('.form_date').datetimepicker({
        language: 'zh-CN',
        weekStart: 1,
        todayBtn: 1,
        autoclose: 1,
        todayHighlight: 1,
        startView: 2,
        minView: 2,
        forceParse: 0
    });

    $('form').validate({
            onKeyup: true,
            eachValidField: function () {
                $(this).closest('div').removeClass('has-error').addClass('has-success');
            },
            eachInvalidField: function () {
                $(this).closest('div').removeClass('has-success').addClass('has-error');
            }
    });
});