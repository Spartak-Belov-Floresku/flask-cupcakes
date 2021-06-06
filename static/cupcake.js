const $ul_1 = $("#list_cupcakes")
const $ul_2 = $("#find_list_cupcakes")
const $form = $('#form')
const $btn_cupcakes_rquest = $(('#cupcakes_rquest'))
const $find_cupcakes = $('#find_cupcakes_fild')


const cupcakes = new fetchAllCupcakes()
cupcakes.createLists($ul_1)

const addCupcake = new createCupcake()
$form.submit((e) =>{
    e.preventDefault();
    addCupcake.sendData($form, $ul_1);
    $form.trigger('reset');
});

const find_cupcakes = new findCupcakes()
$btn_cupcakes_rquest.on('click', () =>{
    find_cupcakes.sendRequest($find_cupcakes, $ul_2)
})