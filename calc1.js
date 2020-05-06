// вводит пользователь
let summa = 650000;
let rate = 0.11;
let period = 120;

// получу из базы

// Вступительный взнос:
let egem_chlens_vzn = 1500
// Ежемесячный членский взнос:
// Минимальный ежемесячный паевый взнос:
// Переплата при ипотечном кредитовании:

let table = document.querySelector(".table");
let str = "<table><tr><th>Месяц</th><th>Долг</th><th>Членский взнос</th><th>Паевый платеж</th><th>Сумма оплат</th></tr>"

// Для ЛК
let summary_credit = + (summa - (summa * rate)).toFixed(0);
let paev_vz = + ((summa - (summa * rate)) / period).toFixed(0);
console.log("сумма кредита: " + summary_credit);
console.log("ежемесячный платеж: " + paev_vz);
let num_mes = 1
let summa_platega = egem_chlens_vzn + paev_vz

for (let i = 0; i < period; i++) {
    str += `<tr><td>${num_mes++}</td><td>${summary_credit}</td>`;
    // console.log(
    //     "месяц: " + i,
    //     "долг: " + summary_credit,
    //     "членский взнос: ",
    //     "паевый платеж: " + paev_vz,
    //     "сумма оплат: ",);
    summary_credit -= paev_vz;
    str += `<td>${egem_chlens_vzn}</td><td>${paev_vz}</td><td>${summa_platega}</td></tr>`;
    // console.log(summary_credit.toFixed(2))
}
str += "</table>";
table.innerHTML = str;

// Аннуитентный кредит
let ann = 0;
let monthRate = rate / 12;
let topPart = +(summa * monthRate).toFixed(2);
console.log(topPart)
let bottomPart = +(1 - (1 / Math.pow(monthRate + 1, period))).toFixed(2);
console.log(bottomPart)
ann = +(topPart / bottomPart).toFixed(2)
console.log(ann);
//
// // Дифференцированный кредит
// let dif = 0;
// let persents = 0;
// let remainSumma = summa;
// let mainDebt = summa / period;
// for (let i = 0; i < period; i++) {
//     console.log("долг: " + remainSumma);
//     persents = remainSumma * monthRate;
//     console.log("проценты: " + persents);
//     remainSumma -= mainDebt
// }