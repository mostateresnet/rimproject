let storage_form = (id, model = '', size = '') => `<div class='small-4 large-4 addcell cell'>
        <label>Storage #${id + 1}</label>
        <input id="storage_model_${id}" type="text" placeholder="Model" value="${model}"/>
        <input id="storage_size_${id}" type="text" placeholder="Size" value="${size}" />
        </div>`;
let gpu_form = (id, name = '') => `<div class='small-4 large-4 addcell cell'>
        <label>GPU #${id + 1}</label>
        <input id="gpu_name_${id}" type="text" placeholder="Name" value="${name}"/>
        </div>`;
let nic_form = (id, mac = '', name = '', type = '') => `<div class='small-4 large-4 addcell cell'>
        <label>Network Card #${id + 1}</label>
        <input id="nic_mac_${id}" type="text" placeholder="MAC" value="${mac}"/>
        <input id="nic_name_${id}" type="text" placeholder="Name" value="${name}" />
        <input id="nic_type_${id}" type="text" placeholder="Type" value="${type}" />
        </div>`;
let display_form = (id, height = '', manufacturer = '', code = '', resolution = '', serial = '', name = '', width = '') => `<div class='small-4 large-4 addcell cell'>
        <label>Display #${id + 1}</label>
        <input id="display_height_${id}" type="text" placeholder="Height in MM" value="${height}"/>
        <input id="display_manufacturer_${id}" type="text" placeholder="Manufacturer" value="${manufacturer}" />
        <input id="display_code_${id}" type="text" placeholder="Product Code" value="${code}" />
        <input id="display_resolution_${id}" type="text" placeholder="Resolution" value="${resolution}" />
        <input id="display_serial_${id}" type="text" placeholder="Serial No" value="${serial}" />
        <input id="display_name_${id}" type="text" placeholder="Name" value="${name}" />
        <input id="display_width_${id}" type="text" placeholder="Width in MM" value="${width}" />
        </div>`;

let storages = 0, gpus = 0, nics = 0, displays = 0;

function populateInputs() {
    for (const s of json_fields['storage'])
        document.getElementById('storage_inputs').innerHTML += storage_form(storages++, s['Model'], s['Size']);

    for (const g of json_fields['GPU'])
        document.getElementById('gpu_inputs').innerHTML += gpu_form(gpus++, g['Name']);

    for (const n of json_fields['network_cards'])
        document.getElementById('nic_inputs').innerHTML += nic_form(nics++, n['MAC'], n['Name'], n['Type']);

    for (const d of json_fields['displays'])
        document.getElementById('display_inputs').innerHTML += display_form(displays++, d["HeightInMillimeters"],
            d["ManufacturerName"], d["ProductCodeID"], d["Resolution"], d["SerialNumberID"], d["UserFriendlyName"],
            d["WidthInMillimeters"]);
}

function addInputs(field) {
    switch (field) {
        case 'storage': document.getElementById('storage_inputs').innerHTML += storage_form(storages++);
            break;
        case 'gpu': document.getElementById('gpu_inputs').innerHTML += gpu_form(gpus++);
            break;
        case 'nic': document.getElementById('nic_inputs').innerHTML += nic_form(nics++);
            break;
        case 'display': document.getElementById('display_inputs').innerHTML += display_form(displays++);
            break;

    }
}

function submitAddEditForm() {
    let storage_json = [], gpu_json = [], nic_json = [], display_json = [];

    for (let i = 0; i < storages; i++) {
        const st_model = document.getElementById('storage_model_' + i).value;
        const st_size = document.getElementById('storage_size_' + i).value;
        if (st_model || st_size)
            storage_json.push({
                "Model": st_model,
                "Size": st_size
            });
    }

    for (let i = 0; i < gpus; i++)
        if (document.getElementById('gpu_name_' + i).value)
            gpu_json.push({ "Name": document.getElementById('gpu_name_' + i).value });

    for (let i = 0; i < nics; i++) {
        const n_mac = document.getElementById('nic_mac_' + i).value;
        const n_name = document.getElementById('nic_name_' + i).value;
        const n_type = document.getElementById('nic_type_' + i).value;
        if (n_mac || n_name || n_type)
            nic_json.push({
                "MAC": n_mac,
                "Name": n_name,
                "Type": n_type
            });
    }

    for (let i = 0; i < displays; i++) {

        const d_height = document.getElementById('display_height_' + i).value;
        const d_manufacturer = document.getElementById('display_manufacturer_' + i).value;
        const d_code = document.getElementById('display_code_' + i).value;
        const d_res = document.getElementById('display_resolution_' + i).value;
        const d_serial = document.getElementById('display_serial_' + i).value;
        const d_name = document.getElementById('display_name_' + i).value;
        const d_width = document.getElementById('display_width_' + i).value;

        if (d_height || d_manufacturer || d_code || d_res || d_serial || d_name || d_width)
            display_json.push({
                "HeightInMillimeters": d_height,
                "ManufacturerName": d_manufacturer,
                "ProductCodeID": d_code,
                "Resolution": d_res,
                "SerialNumberID": d_serial,
                "UserFriendlyName": d_name,
                "WidthInMillimeters": d_width
            });
    }
    dynamic_json = { "storage": storage_json, "GPU": gpu_json, "network_cards": nic_json, "displays": display_json }
    document.getElementById('id_json_fields').value = JSON.stringify(dynamic_json);
    document.add_edit_form.submit();
}

$(document).ready(populateInputs);
