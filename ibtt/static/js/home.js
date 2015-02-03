/**
 * Created by lishaohua on 15-1-22.
 */
$(function (){
    var ghostNode = $('#masonry_ghost').find('.thumbnail'), i, ghostIndexArray = [];
    var ghostCount = ghostNode.length;
    for (i = 0; i < ghostCount; i++) {
        ghostIndexArray[i] = i;
    }
    ghostIndexArray.sort(function (a, b) {
        if (Math.random() > 0.5) {
            return a - b;
        } else {
            return b - a;
        }
    });

    var currentIndex = 0;
    var masNode = $('#masonry');
    var imagesLoading = false;


    function getNewItems() {
        var newItemContainer = $('<div/>');
        for (var i = 0; i < 6; i++) {
            if (currentIndex < ghostCount) {
                newItemContainer.append(ghostNode.get(ghostIndexArray[currentIndex]));
                currentIndex++;
            }
        }
        return newItemContainer.find('.thumbnail');
    }

    function processNewItems(items) {
        items.each(function () {
            var $this = $(this);
            var imgsNode = $this.find('.imgs');
            var title = $this.find('.title').text();
            var author = $this.find('.author').text();
            title += '&nbsp;&nbsp;(' + author + ')';
            var lightboxName = 'lightbox_'; // + imgNames[0];

            var imgNames = imgsNode.find('input[type=hidden]').val().split(',');
            $.each(imgNames, function (index, item) {
                imgsNode.append('<a href="http://fineui.com/case/images/large/' + item + '" data-lightbox="' + lightboxName + '" title="' + title + '"><img src="http://fineui.com/case/images/' + item + '" /></a>');
            });
        });
    }

    function initMasonry() {
        var items = getNewItems().css('opacity', 0);
        processNewItems(items);
        masNode.append(items);

        imagesLoading = true;
        items.imagesLoaded(function () {
            imagesLoading = false;
            items.css('opacity', 1);
            masNode.masonry({
                itemSelector: '.thumbnail',
                isFitWidth: true
            });
        });
    }


    function appendToMasonry() {
        var items = getNewItems().css('opacity', 0);
        processNewItems(items);
        masNode.append(items);

        imagesLoading = true;
        items.imagesLoaded(function () {
            imagesLoading = false;
            items.css('opacity', 1);
            masNode.masonry('appended', items);
        });
    }


    initMasonry();

    $(window).scroll(function () {

        if ($(document).height() - $(window).height() - $(document).scrollTop() < 10) {

            if (!imagesLoading) {
                appendToMasonry();
            }

        }

    });

    function randomColor() {
        var rand = Math.floor(Math.random() * 0xFFFFFF).toString(16);
        for (; rand.length < 6;) {
            rand = '0' + rand;
        }
        return '#' + rand;
    }
});