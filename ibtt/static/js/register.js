/**
 * Created by 001350 on 2015/2/9.
 */
$(function () {

    var register_forms = $('[name="register_form"]');

    //初始化注册modal显示
    $('#header_register_a').on('click', function() {
        register_forms.css('display', 'none');
        $(register_forms[0]).css('display', 'block');
    });
    //下一步按钮事件添加
    $('[name="next_btn"]').on('click', function() {
        var index = this.tabIndex;
        var current_form = $(register_forms[index]);
        current_form.slideUp('normal', function() {
            current_form.find('input').popover('destroy');
        });
        var next_form = $(register_forms[index + 1]);
        next_form.slideDown();
    });

    $('#simple_info_form').on('submit', function() {
        var $form = $(this);
        $form.ajaxSubmit({
                type: 'post',
                url: 'register_base_info/',
                dataType: "json",
                success: function(data) {
                    if(data.success) {
                        alert('注册成功,请继续');
                        $form.slideUp();
                        $form.parent().find('+div>form').slideDown();
                    } else {
                        alert('data.msg');
                    }
                },
                error: function(data) {
                    alert(data);
                }
            });
        return false;
    });

});