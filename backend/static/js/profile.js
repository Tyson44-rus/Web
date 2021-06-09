$(document).ready(() => {
    let formData = new FormData();
    formData.append('id', localStorage.id);

    $.ajax({
        type: "POST",
        url: "/profile",
        data: formData,
        contentType: false,
        processData: false,
        cache: false,
        success: function (data) {
            console.log(data);
            let request = JSON.parse(data);

            console.log(request);
        },
        error: function (data) {
            let request = JSON.parse(data);
            alert(request["result"]);
            console.log(request);
        }
    })
})
