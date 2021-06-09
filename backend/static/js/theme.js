let OPTIONS = {secure: false, domain: "", path:"/"}
var flag = true;

function getCookie(name) {
    let matches = document.cookie.match(new RegExp(
        "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
    ));
    return matches ? decodeURIComponent(matches[1]) : undefined;
}

function setCookie(name, value, options = {}) {

    if (options.expires instanceof Date) {
        options.expires = options.expires.toUTCString();
    }

    let updatedCookie = encodeURIComponent(name) + "=" + encodeURIComponent(value);

    for (let optionKey in options) {
        updatedCookie += "; " + optionKey;
        let optionValue = options[optionKey];
        if (optionValue !== true) {
            updatedCookie += "=" + optionValue;
        }
    }
    document.cookie = updatedCookie;
}

function changeTheme() {
    let elem = $("#css_theme");
    if (flag) {
        flag = false;
        // $.post("./php/theme.php", {"theme": "1"});

        elem.attr("href", "static/styles/base_2.css");
    } else {
        flag = true;
        // $.post("./php/theme.php", {"theme": "0"});

        elem.attr("href", "static/styles/base1.css");
    }
}


$(document).ready(() => {
    // $.get("./php/theme.php", function (data) {
    //     flag = data == "1" ? false : true;
    //
    //     let elem = $("#css_theme");
    //     if (flag){
    //         elem.attr("href", "/styles/base1.styles");
    //     }
    //     else{
    //         elem.attr("href", "/styles/base_2.styles");
    //     }
    // });

    $("#theme").click(changeTheme);
})

