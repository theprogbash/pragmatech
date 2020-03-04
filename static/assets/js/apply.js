$(document).ready(function () {
    $(".apply-btn").click(function () {
        $(".apply-overlay").css("display", "flex");
    });

    $(".send-btn").click(function () {
        $(".apply-overlay").css("display", "none");
    });

    $(".close-btn").click(function () {
        $(".apply-overlay").css("display", "none");
    });

    $(document).click(function (e) {
        if ($(e.target).is('.apply-overlay')) {
            $('.apply-overlay').css("display", "none");
        }
    });
});