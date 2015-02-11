/**
 * Created by 001350 on 2015/2/10.
 */

$(function () {

        $("header").headroom();
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
    //全局的系统校验
    $('form').validate({
            onKeyup: true,
            eachValidField: function () {
                $(this).closest('div').removeClass('has-error').addClass('has-success');
                $(this).popover('destroy');
            },
            eachInvalidField: function (event, status, options) {
                $(this).closest('div').removeClass('has-success').addClass('has-error');
                $(this).popover('destroy');
                var errorMsg = $(this).attr('placeholder');
                if(!status.required) {
                    errorMsg = '请输入' + errorMsg;
                } else if(!status.pattern){
                    errorMsg = errorMsg + '格式不正确';
                }
                var options = {
                    content: errorMsg,
                    container: 'body',
                    placement: 'right'
                }
                $(this).popover(options);
                $(this).popover('toggle');
            }
    });

    $('[role="dialog"]').on('hide.bs.modal', function (e) {
        $(this).find('input').popover('destroy');
    });
});