$(document).ready(() => {

    $("#form").submit((event) => {
        event.preventDefault();

        let formData = new FormData();
        formData.append('credentials', $("#credentials").val());
        formData.append('password', $("#password").val());

        $.ajax({
            type: "POST",
            url: "/auth",
            data: formData,
            contentType: false,
            processData: false,
            cache: false,
            success: function (data) {
                let request = JSON.parse(data);
                alert("Вы авторизовались! Добро пожаловать!");
                window.location.replace("/profile");
            },
            error: function (request) {
                alert("Проблема с авторизацией! Проверьте свои поля!")
                console.log(request);
            }
        })

    })
})
