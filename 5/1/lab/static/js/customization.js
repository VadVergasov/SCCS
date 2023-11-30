document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('settingsForm');
    const fontSizeCheckbox = document.getElementById('fontSizeCheckbox');
    const textColorCheckbox = document.getElementById('textColorCheckbox');
    const backgroundColorCheckbox = document.getElementById('backgroundColorCheckbox');

    function createInput(labelText, inputType, inputId) {
        const label = document.createElement('label');
        label.textContent = labelText;

        const input = document.createElement('input');
        input.type = inputType;
        input.id = inputId;

        label.appendChild(input);
        form.appendChild(label);

        return input;
    }

    fontSizeCheckbox.addEventListener('change', function () {
        const fontSizeInput = document.getElementById('fontSizeInput');
        if (fontSizeCheckbox.checked) {
            if (!fontSizeInput) {
                createInput('Размер шрифта (px):', 'number', 'fontSizeInput');
                document.getElementById('fontSizeInput').addEventListener('input', function () {
                    if (fontSizeCheckbox.checked) {
                        const fontSize = document.getElementById('fontSizeInput').value + 'px';
                        document.body.style.fontSize = fontSize;
                    }
                });
            }
        } else {
            if (fontSizeInput) {
                form.removeChild(fontSizeInput.parentElement);
                document.body.style.fontSize = '';
            }
        }
    });

    textColorCheckbox.addEventListener('change', function () {
        const textColorInput = document.getElementById('textColorInput');
        if (textColorCheckbox.checked) {
            if (!textColorInput) {
                createInput('Цвет текста:', 'color', 'textColorInput');
                document.getElementById('textColorInput').addEventListener('input', function () {
                    if (textColorCheckbox.checked) {
                        const textColor = document.getElementById('textColorInput').value;
                        document.body.style.color = textColor;
                    }
                });
            }
        } else {
            if (textColorInput) {
                form.removeChild(textColorInput.parentElement);
                document.body.style.color = '';
            }
        }
    });

    backgroundColorCheckbox.addEventListener('change', function () {
        const backgroundColorInput = document.getElementById('backgroundColorInput');
        if (backgroundColorCheckbox.checked) {
            if (!backgroundColorInput) {
                createInput('Цвет фона:', 'color', 'backgroundColorInput');
                document.getElementById('backgroundColorInput').addEventListener('input', function () {
                    if (backgroundColorCheckbox.checked) {
                        const backgroundColor = document.getElementById('backgroundColorInput').value;
                        document.body.style.background = backgroundColor;
                    }
                });
            }
        } else {
            if (backgroundColorInput) {
                form.removeChild(backgroundColorInput.parentElement);
                document.body.style.background = 'linear-gradient(to bottom, #222222, #000000)';
            }
        }
    });
});
