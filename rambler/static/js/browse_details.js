$(function () {
    initTable();
});

$(document).ready(function () {
    $('#browse_type').change(function () {
        change_browse();
    });
    $('#browse_select').change(function () {
        change_browse();
    });
    $('#browse_sort').change(function () {
        var browse_sort = $("#browse_sort").val();
        switch (browse_sort) {
            case '0':
                $('#table').bootstrapTable('refreshOptions', {sortName: ''});
                break;
            case '1':
                $('#table').bootstrapTable('refreshOptions', {sortName: 'P_value'});
                break;
            case '2':
                $('#table').bootstrapTable('refreshOptions', {sortName: 'FDR(BH)'});
                break;
            case '3':
                $('#table').bootstrapTable('refreshOptions', {sortName: 'FDR(Bonferroni)'});
                break;
        }
    });
    change_browse();
});

function initTable() {
    $('#table').bootstrapTable({
        height: "auto",
        toolbar: '#toolbar',
        pagination: true,
        cache: false,
        sidePagination: 'client',
        pageSize: 10,
        pageList: [10, 20, 30, 50],
        data: [],
        columns: [],
        onSort: function (name, order) {
            switch (name) {
                case 'P_value':
                    $("#browse_sort").val('1');
                    break;
                case 'FDR(BH)':
                    $("#browse_sort").val('2');
                    break;
                case 'FDR(Bonferroni)':
                    $("#browse_sort").val('3');
                    break;
            }
            $("#browse_sort").selectpicker('refresh');
        }
    })
};


function change_browse() {
    console.log('hi');
    var browse_type = $("#browse_type").val();
    var source_type = $("#req_name").val();
    var filter_type = $('#browse_select').val();

    var rl_dr = {
        'Herb': ['Ingredient', 'TCM_symptom', 'MM_symptom'],
        'Ingredient': ['Herb', 'Target'],
        'TCM_symptom': ['Herb', 'MM_symptom'],
        'MM_symptom': ['TCM_symptom', 'Disease'],
        'Target': ['Ingredient', 'Disease'],
        'Disease': ['MM_symptom', 'Target'],
        'Prescription':[]
    };

    var conv_name = {
        'HB': 'Herb',
        'IT': 'Ingredient',
        'PN': 'Prescription',
        'TT': 'Target',
        'DE': 'Disease'
    };

    if (rl_dr[conv_name[source_type.substr(0, 2)]].indexOf(browse_type) >= 0) {
        $("#browse_select").val('0');
        $("#browse_sort").val('0');
        $(".ind_sl").attr("disabled", true);
        $("#browse_select").selectpicker('refresh');
        $("#browse_sort").selectpicker('refresh');

    } else {
        $(".ind_sl").attr("disabled", false);
        $("#browse_select").selectpicker('refresh');
        $("#browse_sort").selectpicker('refresh');
    }

    $('#table').bootstrapTable("refreshOptions", {
        columns: [], data: [], formatNoMatches: function () {
            return "Searching, please wait...";
        }
    });
    $.ajax({
        url: "/detail_ajax",
        type: "post",
        data: {
            rrid: source_type,
            table_name: browse_type,
            filter: filter_type,
        },
        success: function (res) {
            var data = res;
            if (data['data'].length == 0) {
                $('#table').bootstrapTable("refreshOptions", {
                    columns: [], data: [], formatNoMatches: function () {
                        return "No result found.";
                    }
                });
            } else {
                data.columns[0].formatter = aFormatter
                $('#table').bootstrapTable("refreshOptions", {columns: data['columns'], data: data['data']});
            }
        },
        error: function (e) {
            // location.reload(true);
            //alert("The token has expired, please refresh the page.");
        },
    });
};

//添加超链接
function aFormatter(value, row, index) {
    return [
        '<a href="/detail/' + value + '">' + value + '</a>'
    ].join("")
};








