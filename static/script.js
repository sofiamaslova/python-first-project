const minusButtons = document.getElementsByClassName('minus-button');
// const minusButtons = document.querySelector('.minus-button');

const sumRow = document.querySelector('.sum-row');


const decrementAmount = function(event) {
    const closest = event.target.closest('.cart-position');

    const amountElement = closest.querySelector('.amount');
    const priceElement = closest.querySelector('.price');

    const totalRow = closest.querySelector('.total-row');
    let num = parseInt(amountElement.innerHTML);
    const price = parseInt(priceElement.innerHTML);
    let sum = parseInt(sumRow.innerHTML);
    amountElement.innerHTML = --num;
    totalRow.innerHTML = num * price;
    sumRow.innerHTML = sum - price;


}


Array.from(minusButtons).forEach((button) => {

    button.addEventListener('click', decrementAmount);
});

const plusButtons = document.getElementsByClassName('plus-button');
// const plusButtons = document.querySelector('.plus-button');

const plusAmount = function(event) {
    const closest = event.target.closest('.cart-position');

    const amountElement = closest.querySelector('.amount');
    const priceElement = closest.querySelector('.price');

    const totalRow = closest.querySelector('.total-row');
    let num = parseInt(amountElement.innerHTML);
    const price = parseInt(priceElement.innerHTML);
    let sum = parseInt(sumRow.innerHTML);
    amountElement.innerHTML = ++num;
    totalRow.innerHTML = num * price;
    sumRow.innerHTML = sum + price;




}

Array.from(plusButtons).forEach((button) => {
        button.addEventListener('click', plusAmount);
});


