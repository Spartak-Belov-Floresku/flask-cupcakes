BASE_URL = '/'


class fetchAllCupcakes{

    async fetchCupcakes(){

        return await axios.get(
            `${BASE_URL}api/cupcakes`
        ).then(resp => {
            return resp;
        }).catch(err => {
            console.log(err);
        });

    }
    
    async createLists(ul){
        const responce = await this.fetchCupcakes()
        for(let cupcake of responce.data.cupcakes){
            ul.append(`<li class="list-group-item list-group-item-secondary">Flavor : ${cupcake.flavor}
            <img src="${cupcake.image}" class="w-25 img-thumbnail rounded float-right"><br> 
            Rating: ${cupcake.rating}</li>`)
        }
    }
}


class createCupcake{

    getData(form){
        return form.serializeArray().reduce((obj, item) => {
            obj[item.name] = item.value;
            return obj;
        }, {});
    }

    async sendData(form, ul){
        const json = this.getData(form);
        const responce = await axios.post(`${BASE_URL}api/cupcakes`,{
                                json
                            }).then( responce => {
                                    return responce
                            }).catch(err => {
                                    console.log(err)
                            });
        const cupcake = responce.data.cupcake
        ul.append(`<li class="list-group-item list-group-item-secondary">Flavor : ${cupcake.flavor}
                    <img src="${cupcake.image}" class="w-25 img-thumbnail rounded float-right"><br> 
                    Rating: ${cupcake.rating}</li>`)
    }
}


class findCupcakes{

    async sendRequest(inp, ul){
        let val = inp.val()
        const responce = await axios.get(`${BASE_URL}api/cupcakes/find`, {
            params: {find: val}
        }).then(resp => {
            return resp;
        }).catch(err => {
            console.log(err);
        });

    
        for(let cupcake of responce.data.cupcakes){
            ul.append(`<li class="list-group-item list-group-item-secondary">Flavor : ${cupcake.flavor}
            <img src="${cupcake.image}" class="w-25 img-thumbnail rounded float-right"><br> 
            Rating: ${cupcake.rating}</li>`)
        }



    }
}