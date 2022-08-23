< !DOCTYPE
html >
< html
lang = "en" >
< head >
< meta
charset = "UTF-8" > < / meta >

< link
rel = "stylesheet"
href = "css/style.css"
> < / link >

< title > Learn
JS < / title >
< / head >

< body >
< script
src = "js/jquery-1.12.0.min.js" > < / script >

< div


class ="container" >

< p > 1 < / p >
< p > 2 < / p >
< p > 3 < / p >
< button
id = "btn" > Жми < / button >
< input
id = "num"
type = "text"
value = "" >
< script >

var
elem = document.getElementsByTagName('p');
var
btn = document.getElementById('btn');
btn.addEventListener('click', func);

function
func()
{
    var
arr2 = [];
for (var i = 0; i < elem.length; i++)
{
    arr2[i] = elem[i].innerHTML;
console.log(arr2[i]);
}

var
input = document.getElementById('num');
input.value = arr2.sort();
}

// function
sortArr(a, b)
{
// if (a > b)
{
//
return -1;
//}
// if (a < b) {
// return -1;
//}
// if (a == b) {
// return 0;
//}
//}

// for (var i = 1; i <= 9; i++) {
                                //     for (var j = 1; j <= 4; j++) {
// document.write(i); // выводит
'111', потом
'222', потом
'333'
и
так
далее
//}
//}

// var
a = 3;
// document.write(a);
// document.write('<br/>');
// // // // // // // // // // // // //
// var
b = 5;
// var
c = 6;
// document.write(b + c);
// document.write('<br/>');
// document.write(b * c);
// document.write('<br/>');
// document.write(b / c);
// document.write('<br/>');
// // // // // // // // // // // // //
// var
d = 10;
// var
e = 20;
// var
result = (d + e);
// document.write(result);
// document.write('<br/>');
// // // // // // // // // // // // //
// var
g = 15;
// var
h = 18;
// var
c = (g - h);
// var
k = 10;
// var
result = (c + k);
// document.write(result);

// Задача_1
   // var
obj = {a: 1, b: 2, c: 3};
// document.write(obj['c']);
// document.write(obj.c);
// document.write('<br/>');

// Задача_2
   // var
obj = {Коля: '1000', Вася: '500', Петя: '200'};
// document.write(obj['Коля'] + ', ' + obj['Петя']);
// document.write('<br/>');

// Задача_3
   // var
obj = {1: 'Понедельник', 2: 'Вторник', 3: 'Среда', 4: 'Четверг', 5: 'Пятница', 6: 'Суббота', 7: 'Воскресенье'};
// document.write(obj['1']);
// document.write('<br/>');

// Задача_4
   // var
obj = {1: 'Понедельник', 2: 'Вторник', 3: 'Среда', 4: 'Четверг', 5: 'Пятница', 6: 'Суббота', 7: 'Воскресенье'};
// var
day = 3;
// document.write(obj[day]);
// document.write('<br/>');

// Задачи
по
многомерным
массивам
// Задача_1
// var
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];
// document.write(arr[1][0]);
// document.write('<br/>');

// Задача_2
   // var
lang = {js: ['jQuery', 'Angular'], php: 'hello', css: 'world'};
// document.write(lang['js'][0]);
// document.write('<br/>');

// Задача_3
   // var
days = {
       // ru:['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье'],
// en: ['Monday', 'Tyesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
       //};
// document.write(days['ru'][0] + ', ' + days['en'][2]);
// document.write('<br/>');

// Задача_4
   // var
days = {
       // ru:['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье'],
// en: ['Monday', 'Tyesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
       //};
// var
lang = days.ru;
// var
day = 2;
// document.write(lang[day]);
// document.write('<br/>');

/ *IF
ELSE
== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == = * /
// http: // theory.phphtml.net / tasks / javascript / base / rabota - s - konstrukciyami - if - else -switch - case - v - javascript.html

                                                                                                     // var
a = 4;
// if (a == 0 | | a == 2){
// var a = a + 7;
// document.write(a);
//}
// else {
// var a = a / 7;
// document.write(a);
//}

// var num = 2;
// switch (num){
// case 1: result = 'зима';
//
break;
// case
2: result = 'весна';
// break;
// case
3: result = 'лето';
// break;
// case
4: result = 'осень';
// break;
//}
// document.write(result);
// document.write('<br/>');

// Задача_16
   // var
day = 23;
// if (day <= 10){
// var
decad = 1;
//}
// if (day >= 11 & & day <= 20){
// var
decad = 2;
//}
// if (day >= 21 & & day <= 30){
// var
decad = 3;
//}
// document.write(decad);
// document.write('<br/>');

// // Задача_17
      // var
month = 11;
// if (month == 12 | | month <= 2){
// var
result = 'Зима';
//}
// if (month >= 3 & & month <= 5){
// result = 'весна';
//}
// if (month >= 6 & & month <= 8){
// result = 'лето';
//}
// if (month >= 9 & & month <= 11){
// result = 'осень';
//}
// document.write(result);
// document.write('<br/>');

// // Задача_18 - Эту
задачу
не
смог
решить, но
логику
понял
// var
year = 2000;
// if (year % 4 == 0 | | (year % 400 == 0 & & year % 100 != 0)) {
// document.write('Високосный');
//} else {
// document.write('Не високосный');
//}
// document.write('<br/>');

// // Задача_19
      // var
symbol = 'abcde';
// if (symbol.charAt(0) === 'a'){
// document.write('да');
//}
// else {
// document.write('нет');
//}
// document.write('<br/>');

// // Задача_20
      // var
number = '12345';
// if (number.charAt(0) == '1' | | number.charAt(0) == '2' | | number.charAt(0) == '3'){
// document.write('да');
//}
// else {
// document.write('нет');
//}
// document.write('<br/>');

// // Задача_21(2
варианта) Мне
кажется
тут
я
написал
гавнокод, жду
комментарий)
// var
numb = '123';
// // result = + numb.charAt(0) + + numb.charAt(1) + + numb.charAt(2);
// result = Number(numb.charAt(0)) + Number(numb.charAt(1)) + Number(numb.charAt(2));
// document.write(result);
// document.write('<br/>');

// // Задача_22
      // var
num = '222222';
// result_1 = Number(num.charAt(0)) + Number(num.charAt(1)) + Number(num.charAt(2));
// result_2 = Number(num.charAt(3)) + Number(num.charAt(4)) + Number(num.charAt(5));
// if (result_1 == result_2){
// document.write('да');
//}
// else {
// document.write('нет');
//}
// document.write('<br/>');

// // Задача_23
// var domen = 'http://phphtml.net';
// if (domen[0] == 'h' & & domen[1] == 't' & & domen[2] == 't' & & domen[3] == 'p'){
// document.write('да');
//}
// else {
// document.write('нет');
//}
// document.write('<br/>');

/ * for
while
    http: // theory.phphtml.net / books / javascript / base / rabota - s - ciklami -
    for -i -while -v-javascript.html
    == == == == == == == == == == == == == == == == == == == = * /
    // var
    num = 1;

    // while (num <= 100){
    // document.write(num+'<br>');
    // num ++;
    //}

    // for (var num = 1; num <= 100; num++){
                                           // document.write(num + '<br>');
    //}

    // for (var num = 11; num <= 33; num++){
                                           // document.write(num + '<br>');
    //}

    // var
    num = 11;

    // while (num <= 33){
    // document.write(num+'<br>');
    // num ++;
    //}

    // var
    num = 1;
    // while (num < 100){
    // if (num % 2 == = 0){
    // document.write(num+'<br>');
    // }
    // 	num++;
    // }

    //  С помощью цикла найдите сумму чисел от 1 до 100.
    // var num = 1;
    // var result = 1;
    // for (var num = 0; num < 100;	num++){
                                             // 	result = result + num;
    // }
    // document.write(result);
    // document.write('<br>');

    //  Дан массив с элементами [1, 2, 3, 4, 5]. С помощью цикла for выведите все эти элементы на экран
    // var arr = ['1' ,'2' ,'3' ,'4' ,'5'];
    // for (var i =0; i < arr.length; i++){
                                          // 	document.write(arr[i]);
    // }

    / /Дан массив с элементами [1, 2, 3, 4, 5]. С помощью цикла for найдите сумму элементов этого массива. Запишите ее в переменную result
    // var arr = [1 ,2 ,3 ,4 ,5];
    // var result = 0;
    // for (var i =0; i < arr.length; i++){
                                          // 	result = result + arr[i];
    // }
    // document.write(result);

    //  Дан объект obj. С помощью первого цикла fo r -in выведите на экран ключи, с помощью второго - элементы.
    // var obj = {green: 'зеленый', red: 'красный', blue: 'голубой'}
    // for (key in obj) {
                        // 	document.write(key + ', ');
    // }
    // for (key in obj) {
                        // 	document.write(obj[key] + ', ');
    // }
    // document.write('<br/>');