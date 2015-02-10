/**
 * Created by 001350 on 2015/2/9.
 */
$(function () {
    var regster_forms = $('[name="register_form"]');

    $('[name="next_btn"]').on('click', function() {
        var next_btn = $(this);
        var index = this.tabIndex;
        var current_form = $(regster_forms[index]);
        current_form.fadeIn()
        var next_form = $(regster_forms[index + 1]);
        next_form.fadeOut();
    });


});