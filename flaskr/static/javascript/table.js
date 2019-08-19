$(document).ready(function() {
    $('.data-cell').each(function() {
        var green_strength = $(this).text();
        $(this).css('background-color', 'rgb(' + 255 * (1 - green_strength) + ', 255, ' + 255 * (1 - green_strength) + ')');
    });
});