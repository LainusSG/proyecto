var divMas=document.getElementById("mas");
function btnMinformacion(){
var mTable=` <table class="u-table-entity">
<colgroup>
  <col width="10%">
  <col width="16%">
  <col width="30%">
  <col width="19%">
  <col width="12%">
  <col width="12%">
</colgroup>
<thead class="u-custom-color-3 u-table-header u-table-header-1">
  <tr style="height: 59px;">
    <th class="u-border-1 u-border-grey-50 u-table-cell">ID</th>
    <th class="u-border-1 u-border-grey-50 u-table-cell">Nombre</th>
    <th class="u-border-1 u-border-grey-50 u-table-cell">Descripción</th>
    <th class="u-border-1 u-border-grey-50 u-table-cell">Marca</th>
    <th class="u-border-1 u-border-grey-50 u-table-cell">Cantidad</th>
    <th class="u-border-1 u-border-grey-50 u-table-cell">Caducidad</th>
  </tr>
</thead>
<tbody class="u-table-body">
  <tr style="height: 75px;">
    <td class="u-border-1 u-border-grey-40 u-border-no-left u-border-no-right u-table-cell">0001</td>
    <td class="u-border-1 u-border-grey-40 u-border-no-left u-border-no-right u-table-cell">Pinza Halsted</td>
    <td class="u-border-1 u-border-grey-40 u-border-no-left u-border-no-right u-table-cell">Description</td>
    <td class="u-border-1 u-border-grey-40 u-border-no-left u-border-no-right u-table-cell">Description</td>
    <td class="u-border-1 u-border-grey-40 u-border-no-left u-border-no-right u-table-cell">1</td>
    <td class="u-border-1 u-border-grey-40 u-border-no-left u-border-no-right u-table-cell"></td>
  </tr>
  <tr style="height: 76px;">
    <td class="u-border-1 u-border-grey-40 u-border-no-left u-border-no-right u-table-cell">0002</td>
    <td class="u-border-1 u-border-grey-40 u-border-no-left u-border-no-right u-table-cell">Description</td>
    <td class="u-border-1 u-border-grey-40 u-border-no-left u-border-no-right u-table-cell">Description</td>
    <td class="u-border-1 u-border-grey-40 u-border-no-left u-border-no-right u-table-cell">Description</td>
    <td class="u-border-1 u-border-grey-40 u-border-no-left u-border-no-right u-table-cell">3</td>
    <td class="u-border-1 u-border-grey-40 u-border-no-left u-border-no-right u-table-cell"></td>
  </tr>
  <tr style="height: 76px;">
    <td>0003</td>
    <td>Description</td>
    <td >Description</td>
    <td >Description</td>
    <td >4</td>
    <td ></td>
  </tr>
  <tr style="height: 76px;">
    <td >0004</td>
    <td>Description</td>
    <td >Description</td>
    <td >Description</td>
    <td>2</td>
    <td ></td>
  </tr>
</tbody>
</table>`;
divMas.innerHTML=mTable;

}