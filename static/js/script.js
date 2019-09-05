// To toggle the show/hide details button to display/hide the review details
$(".show-details").on("click", function() {
    if ($(".reviews")[0].style.display === "none") {
        $(".reviews")[0].style.display = "block";
    }
    else {
        $(".reviews")[0].style.display = "none";
    }
});