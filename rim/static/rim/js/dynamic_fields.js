let storage_form = (id, model, size) => `<div class='small-4 large-4 addcell cell'>
        <label>Storage #${id + 1}</label>
        <input id="storage_model_${id}" type="text" placeholder="Model" value="${model}"/>
        <input id="storage_size_${id}" type="text" placeholder="Size" value="${size}" />
        </div>`;
let gpu_form = (id, name) => `<div class='small-4 large-4 addcell cell'>
        <label>GPU #${id + 1}</label>
        <input id="gpu_name_${id}" type="text" placeholder="Name" value="${name}"/>
        </div>`;
let nic_form = (id, mac, name, type) => `<div class='small-4 large-4 addcell cell'>
        <label>Network Card #${id + 1}</label>
        <input id="nic_mac_${id}" type="text" placeholder="MAC" value="${mac}"/>
        <input id="nic_name_${id}" type="text" placeholder="Name" value="${name}" />
        <input id="nic_type_${id}" type="text" placeholder="Type" value="${type}" />
        </div>`;
let display_form = (id, height, manufacturer, code, resolution, serial, name, width) => `<div class='small-4 large-4 addcell cell'>
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
        case 'storage': document.getElementById('storage_inputs').innerHTML += storage_form(storages++, '', '');
            break;
        case 'gpu': document.getElementById('gpu_inputs').innerHTML += gpu_form(gpus++, '', '');
            break;
        case 'nic': document.getElementById('nic_inputs').innerHTML += nic_form(nics++, '', '', '');
            break;
        case 'display': document.getElementById('display_inputs').innerHTML += display_form(displays++, '', '', '', '', '', '', '');
            break;

    }
}

function submitAddEditForm() {
    let storage_json = [], gpu_json = [], nic_json = [], display_json = [];

    for (let i = 0; i < storages; i++)
        if (document.getElementById('storage_model_' + i).value)
            storage_json.push({
                "Model": document.getElementById('storage_model_' + i).value,
                "Size": document.getElementById('storage_size_' + i).value
            });


    for (let i = 0; i < gpus; i++)
        if (document.getElementById('gpu_name_' + i).value)
            gpu_json.push({ "Name": document.getElementById('gpu_name_' + i).value });

    for (let i = 0; i < nics; i++)
        if (document.getElementById('nic_mac_' + i).value)
            nic_json.push({
                "MAC": document.getElementById('nic_mac_' + i).value,
                "Name": document.getElementById('nic_name_' + i).value,
                "Type": document.getElementById('nic_type_' + i).value
            })

    for (let i = 0; i < displays; i++)
        if (document.getElementById('display_serial_' + i).value)
            display_json.push({
                "HeightInMillimeters": document.getElementById('display_height_' + i).value,
                "ManufacturerName": document.getElementById('display_manufacturer_' + i).value,
                "ProductCodeID": document.getElementById('display_code_' + i).value,
                "Resolution": document.getElementById('display_resolution_' + i).value,
                "SerialNumberID": document.getElementById('display_serial_' + i).value,
                "UserFriendlyName": document.getElementById('display_name_' + i).value,
                "WidthInMillimeters": document.getElementById('display_width_' + i).value
            })

    dynamic_json = { "storage": storage_json, "GPU": gpu_json, "network_cards": nic_json, "displays": display_json }
    document.getElementById('id_json_fields').value = JSON.stringify(dynamic_json);
    document.add_edit_form.submit();
}

setTimeout(() => populateInputs(), 500);
