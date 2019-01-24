const minusButtons = document.getElementsByClassName('minus-button');
// const minusButtons = document.querySelector('.minus-button');

const decrementAmount = function(event) {
    const closest = event.target.closest('.cart-position');
    console.log(closest)
    const amountElement = closest.querySelector('.amount');
    const priceElement = closest.querySelector('.price');
    console.log(priceElement)
    const totalRow = closest.querySelector('.total-row');
    let num = parseInt(amountElement.innerHTML);
    const price = parseInt(priceElement.innerHTML);
    amountElement.innerHTML = --num;
    totalRow.innerHTML = num * price;

    console.log(num)
}


Array.from(minusButtons).forEach((button) => {
    console.log(button)
    button.addEventListener('click', decrementAmount);
});

const plusButtons = document.getElementsByClassName('plus-button');
// const plusButtons = document.querySelector('.plus-button');

const plusAmount = function(event) {
    const closest = event.target.closest('.cart-position');
    console.log(closest)
    const amountElement = closest.querySelector('.amount');
    const priceElement = closest.querySelector('.price');
    console.log(priceElement)
    const totalRow = closest.querySelector('.total-row');
    let num = parseInt(amountElement.innerHTML);
    const price = parseInt(priceElement.innerHTML);
    amountElement.innerHTML = ++num;
    totalRow.innerHTML = num * price;

    console.log(num)
}

Array.from(plusButtons).forEach((button) => {
    console.log(button)
    button.addEventListener('click', plusAmount);
});