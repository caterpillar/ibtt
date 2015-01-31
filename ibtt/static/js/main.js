/**
 * Created by lishaohua on 15-1-22.
 */
require.config({
    paths: {
        "jquery": "jquery-2.1.3.min",
        "bootstrap": "bootstrap.min",
        "jquery_bootstrap": "jquery.bootstrap.min"
    }
});


require(['jquery', 'bootstrap', 'jquery_bootstrap'], function($) {

    var logout_a = $('#logout');
    logout_a.on('click', function() {
        $.messager.model = {
            ok: {text: '确定', classed: 'btn-success'},
            cancel: {text: '取消', classed: ' btn-default'}
        };
        $.messager.confirm('退出', '确定退出dailylog?', function() {
            $.ajax({
                url: '/logout',
                dataType: 'json',
                success: function(data) {
                    window.location = '/login';
                }
            });
        });
    });
});