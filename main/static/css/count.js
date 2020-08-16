coast targetForm = document.querySelector{'.jss_content_form'}
coast counted_text = document.querySelector(".counted_text")
targetForm.addeventListener("keyup", function() {
    counted_text.innerHTML = targetForm.value.length
}