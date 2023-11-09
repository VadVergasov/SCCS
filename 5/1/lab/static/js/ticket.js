const promoCodes = {
    'CODE1': 15, // Скидка 15%
    'CODE2': 20, // Скидка 20%
    'CODE3': 10, // Скидка 10%
    'CODE4': 25, // Скидка 25%
    'CODE5': 30  // Скидка 30%
};

let appliedPromoCode = '';
const ticketPrice = 15;

function applyPromoCode() {
    const promoCodeInput = document.getElementById('promoCode');
    const discountMessage = document.getElementById('discountMessage');

    const enteredPromoCode = promoCodeInput.value.toUpperCase();

    if (promoCodes.hasOwnProperty(enteredPromoCode)) {
        appliedPromoCode = enteredPromoCode;
        discountMessage.textContent = `Промокод "${appliedPromoCode}" применен. Скидка ${promoCodes[appliedPromoCode]}%`;

        const ticketQuantityInput = document.getElementById('ticketQuantity');
        const totalPriceMessage = document.getElementById('totalPriceMessage');

        const ticketQuantity = parseInt(ticketQuantityInput.value);

        if (isNaN(ticketQuantity) || ticketQuantity < 1) {
            totalPriceMessage.textContent = 'Пожалуйста, введите корректное количество билетов.';
            return;
        }

        let discountedPrice = ticketPrice * ticketQuantity;

        if (appliedPromoCode !== '') {
            discountedPrice = discountedPrice - (discountedPrice * promoCodes[appliedPromoCode] / 100);
        }

        totalPriceMessage.value = `${discountedPrice.toFixed(2)}`;
    } else {
        discountMessage.textContent = 'Недействительный промокод';
    }
}

function resetPromoCode() {
    appliedPromoCode = '';
    document.getElementById('promoCode').value = '';
    document.getElementById('discountMessage').textContent = 'Промокод сброшен.';
}

