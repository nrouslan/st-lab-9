document.addEventListener("DOMContentLoaded", function () {
  const loginForm = document.getElementById("loginForm");
  const usernameInput = document.getElementById("username");
  const passwordInput = document.getElementById("password");
  const usernameError = document.getElementById("usernameError");
  const passwordError = document.getElementById("passwordError");
  const successMessage = document.getElementById("successMessage");
  const userInfo = document.getElementById("userInfo");
  const userNameSpan = document.getElementById("userName");
  const logoutButton = document.getElementById("logoutButton");
  const loginButton = document.getElementById("loginButton");

  // Валидные учетные данные для тестирования
  const validCredentials = {
    testuser: "Password123!",
    admin: "AdminPass456!",
    user: "SimplePass789!",
  };

  // Функция валидации формы
  function validateForm() {
    let isValid = true;

    // Валидация имени пользователя
    if (!usernameInput.value.trim()) {
      usernameInput.classList.add("error");
      usernameError.style.display = "block";
      isValid = false;
    } else {
      usernameInput.classList.remove("error");
      usernameError.style.display = "none";
    }

    // Валидация пароля
    if (!passwordInput.value) {
      passwordInput.classList.add("error");
      passwordError.style.display = "block";
      isValid = false;
    } else {
      passwordInput.classList.remove("error");
      passwordError.style.display = "none";
    }

    return isValid;
  }

  // Обработчик отправки формы
  loginForm.addEventListener("submit", function (e) {
    e.preventDefault();

    if (validateForm()) {
      const username = usernameInput.value.trim();
      const password = passwordInput.value;

      loginButton.disabled = true;
      loginButton.textContent = "Вход...";

      // Имитация задержки сети
      setTimeout(() => {
        if (validCredentials[username] === password) {
          // Успешный вход
          showSuccess(username);
        } else {
          // Неверные учетные данные
          showError("Неверное имя пользователя или пароль");
          loginButton.disabled = false;
          loginButton.textContent = "Войти";
        }
      }, 1000);
    }
  });

  // Показать успешный вход
  function showSuccess(username) {
    loginForm.style.display = "none";
    successMessage.style.display = "block";

    setTimeout(() => {
      successMessage.style.display = "none";
      userInfo.style.display = "block";
      userNameSpan.textContent = username;
    }, 2000);
  }

  // Показать ошибку
  function showError(message) {
    const errorDiv = document.createElement("div");
    errorDiv.className = "error-message";
    errorDiv.style.display = "block";
    errorDiv.textContent = message;
    errorDiv.style.marginBottom = "20px";

    loginForm.insertBefore(errorDiv, loginForm.firstChild);

    setTimeout(() => {
      errorDiv.remove();
    }, 3000);
  }

  // Выход из системы
  logoutButton.addEventListener("click", function () {
    userInfo.style.display = "none";
    loginForm.style.display = "block";
    usernameInput.value = "";
    passwordInput.value = "";
    loginButton.disabled = false;
    loginButton.textContent = "Войти";
  });

  // Забыли пароль (заглушка)
  document
    .getElementById("forgotPassword")
    .addEventListener("click", function (e) {
      e.preventDefault();
      alert("Функция восстановления пароля временно недоступна");
    });

  // Регистрация (заглушка)
  document
    .getElementById("registerLink")
    .addEventListener("click", function (e) {
      e.preventDefault();
      alert("Функция регистрации временно недоступна");
    });

  // Валидация в реальном времени
  usernameInput.addEventListener("input", function () {
    if (usernameInput.value.trim()) {
      usernameInput.classList.remove("error");
      usernameError.style.display = "none";
    }
  });

  passwordInput.addEventListener("input", function () {
    if (passwordInput.value) {
      passwordInput.classList.remove("error");
      passwordError.style.display = "none";
    }
  });
});
