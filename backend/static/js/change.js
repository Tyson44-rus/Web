$(document).ready(() => {
    $("#form").submit((event) => {
        event.preventDefault();

        let formData = new FormData();
        formData.append("id",  $("#id-field").val());
        formData.append("name",  $("#name-field").val());
        formData.append("value",  $("#value-field").val());

        $.ajax({
            type: "POST",
            url: "/other",
            data: formData,
            contentType: false,
            processData: false,
            cache: false,
            success: function (data) {
                alert('ok');
                let request = JSON.parse(data);
                console.log(request);
            },
            error: function (data) {
                alert("Вы ввели некоректые данные. Проверьте поля.");
                let request = JSON.parse(data);
                console.log(request);
            }
        })
    })
})