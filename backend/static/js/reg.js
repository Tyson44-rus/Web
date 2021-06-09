$(document).ready(() => {
    $("#form").submit((event) => {
        event.preventDefault();

        //Проверка формы
        let formValid = true,
            password_equal = $("#password").val() == $("#password_check").val();

        if (!password_equal) {
            formValid = false;
            alert("Извините! Пароли не совпадают.");
        }

        let regx = RegExp("(?=.*[0-9])(?=.*[!-.:-@[-`{-~])(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z!-.:-@[-`{-~]{8,}", "gm"),
            password_regExp = regx.exec($("#password").val());

        if (!password_regExp) {
            formValid = false;
            alert("Извините! Ваш пароль должен иметь спец.символы, латинские заглавные и прописные буквы.");
        }

        if (formValid) {
            let formData = new FormData();
            formData.append('firstname', $("#firstname").val());
            formData.append("surname", $("#surname").val())
            formData.append('email', $("#email").val());
            formData.append('login', $("#login").val());
            formData.append('password', $("#password").val());
            formData.append("age", $("#age option:selected").val());
            formData.append("sex", $('input[name=sex]:checked').val())

            $.ajax({
                type: "POST",
                url: "/reg",
                data: formData,
                contentType: false,
                processData: false,
                cache: false,
                success: function (data) {
                    let request = JSON.parse(data);
                    console.log(request);
                    alert(request["result"]);
                    window.location.replace("/auth");
                },
                error: function (data) {
                    alert("Вы ввели некоректые данные. Проверьте поля.");
                    let request = JSON.parse(data);
                    console.log(request);
                }
            })
        }
    })
})
