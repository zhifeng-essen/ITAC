$(function () {
    $('#table').bootstrapTable({
        toolbar: '#toolbar',
        pageNumber: 1,
        pagination: false,
        pageSize: 10,
        pageList: [10, 20, 30, 50],
        data: [],
        columns: [],
    });

    //自动补全实现
    $("#herb_ipt").typeahead({
        source: function (query, process) {
            return $.ajax({
                url: '/search/search_th',
                type: 'post',
                data: {name: query, table_name: 'Herb'},
                success: function (result) {
                    return process(JSON.parse(result));
                },
            });
        },

        updater: function (item) {
            return item;
        },
        displayText: function (item) {
            return item;
        },
        minLength: 1,
        showHintOnFocus: "true",
        fitToElement: true,
        items: 'all',
        autoSelect: true,
        afterSelect: function (item) {
            do_search($("#tf_herb"));
        },
        delay: 500//在查找之间添加延迟
    });

    $("#ing_ipt").typeahead({
        source: function (query, process) {
            return $.ajax({
                url: '/search/search_th',
                type: 'post',
                data: {name: query, table_name: 'Mol'},
                success: function (result) {
                    return process(JSON.parse(result));
                },
            });
        },

        updater: function (item) {
            return item;
        },
        displayText: function (item) {
            return item;
        },
        minLength: 1,
        showHintOnFocus: "true",
        fitToElement: true,
        items: 'all',
        autoSelect: true,
        afterSelect: function (item) {
            do_search($("#tf_ing"));
        },
        delay: 500
    });

    $("#tar_ipt").typeahead({
        source: function (query, process) {
            return $.ajax({
                url: '/search/search_th',
                type: 'post',
                data: {name: query, table_name: 'Gene'},
                success: function (result) {
                    return process(JSON.parse(result));
                },
            });
        },

        updater: function (item) {
            return item;//这里一定要return，否则选中不显示，外加调用display的时候null reference错误。
        },
        displayText: function (item) {
            return item;//返回字符串
        },
        minLength: 1,//键入字数多少开始补全
        showHintOnFocus: "true",//将显示所有匹配项
        fitToElement: true,//选项框宽度与输入框一致
        items: 'all',//下拉选项中出现条目的最大数量。也可以设置为“all”
        autoSelect: true,//允许你决定是否自动选择第一个建议
        afterSelect: function (item) {
            do_search($("#tf_tar"));
        },
        delay: 500//在查找之间添加延迟
    });

    $("#tcm_ipt").typeahead({
        source: function (query, process) {
            return $.ajax({
                url: '/search/search_th',
                type: 'post',
                data: {name: query, table_name: 'TCM_symptom'},
                success: function (result) {
                    return process(JSON.parse(result));
                },
            });
        },

        updater: function (item) {
            return item;//这里一定要return，否则选中不显示，外加调用display的时候null reference错误。
        },
        displayText: function (item) {
            return item;//返回字符串
        },
        minLength: 1,//键入字数多少开始补全
        showHintOnFocus: "true",//将显示所有匹配项
        fitToElement: true,//选项框宽度与输入框一致
        items: 'all',//下拉选项中出现条目的最大数量。也可以设置为“all”
        autoSelect: true,//允许你决定是否自动选择第一个建议
        afterSelect: function (item) {
            do_search($("#tf_tcm"));
        },
        delay: 500//在查找之间添加延迟
    });

    $("#mm_ipt").typeahead({
        source: function (query, process) {
            return $.ajax({
                url: '/search/search_th',
                type: 'post',
                data: {name: query, table_name: 'MM_symptom'},
                success: function (result) {
                    return process(JSON.parse(result));
                },
            });
        },

        updater: function (item) {
            return item;//这里一定要return，否则选中不显示，外加调用display的时候null reference错误。
        },
        displayText: function (item) {
            return item;//返回字符串
        },
        minLength: 1,//键入字数多少开始补全
        showHintOnFocus: "true",//将显示所有匹配项
        fitToElement: true,//选项框宽度与输入框一致
        items: 'all',//下拉选项中出现条目的最大数量。也可以设置为“all”
        autoSelect: true,//允许你决定是否自动选择第一个建议
        afterSelect: function (item) {
            do_search($("#tf_mm"));
        },
        delay: 500//在查找之间添加延迟
    });

    $("#dis_ipt").typeahead({
        source: function (query, process) {
            return $.ajax({
                url: '/search/search_th',
                type: 'post',
                data: {name: query, table_name: 'Disease'},
                success: function (result) {
                    return process(JSON.parse(result));
                },
            });
        },

        updater: function (item) {
            return item;//这里一定要return，否则选中不显示，外加调用display的时候null reference错误。
        },
        displayText: function (item) {
            return item;//返回字符串
        },
        minLength: 1,//键入字数多少开始补全
        showHintOnFocus: "true",//将显示所有匹配项
        fitToElement: true,//选项框宽度与输入框一致
        items: 'all',//下拉选项中出现条目的最大数量。也可以设置为“all”
        autoSelect: true,//允许你决定是否自动选择第一个建议
        afterSelect: function (item) {
            do_search($("#tf_dis"));
        },
        delay: 500//在查找之间添加延迟
    });
});

$(document).ready(function () {
    $('#search_result').hide();
    $("#myTab li").click(function () {
        $("#search_result").hide();
    });

    $("#tf_herb").bind('submit', function () {
        if (document.getElementById("herb_ipt").value == "") {
            $("#herb_ipt").val("qinghao");
        }
        do_search($("#tf_herb"));
        return false;
    });
    $("#tf_pre").bind('submit', function () {
        if (document.getElementById("pre_ipt").value == "") {
            $("#pre_ipt").val("加味参夏汤");
        }
        do_search($("#tf_pre"));
        return false;
    });
    $("#tf_ing").bind('submit', function () {
        if (document.getElementById("ing_ipt").value == "") {
            $("#ing_ipt").val("artemisinin");
        }
        do_search($("#tf_ing"));
        return false;
    });
    $("#tf_tar").bind('submit', function () {
        if (document.getElementById("tar_ipt").value == "") {
            $("#tar_ipt").val("IL6");
        }
        do_search($("#tf_tar"));
        return false;
    });
    $("#tf_dis").bind('submit', function () {
        if (document.getElementById("dis_ipt").value == "") {
            $("#dis_ipt").val("malaria");
        }
        do_search($("#tf_dis"));
        return false;
    });

    $(".herb_example").click(function () {
        $("#herb_ipt").val($(this).text());
    });
    $(".pre_example").click(function () {
        $("#pre_ipt").val($(this).text());
    });
    $(".ing_example").click(function () {
        $("#ing_ipt").val($(this).text());
    });
    $(".tar_example").click(function () {
        $("#tar_ipt").val($(this).text());
    });
    $(".dis_example").click(function () {
        $("#dis_ipt").val($(this).text());
    });

});

function do_search(tf) {
    var tf_data = tf.serializeArray();
    var values = {};
    for (x in tf_data) {
        values[tf_data[x].name] = tf_data[x].value;
    }

    $('#search_result').show();
    $('#table').bootstrapTable("refreshOptions", {
        columns: [], data: [], formatNoMatches: function () {
            return "Searching, please wait...";
        }
    });
    $('#result_key').html('Possible matches for ' + convert_table_name(values['table_name']) + ': <small class="text-danger">' + values['key'] + '</small>');

    $.ajax({
        url: "/search/search_ajax",
        type: "post",
        data: values,
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
                $('#table').bootstrapTable("refreshOptions", {
                    columns: data['columns'],
                    data: data['data'],
                    pageSize: data['data'].length
                });
            }
        },
        error: function (e) {
            // alert("something wrong...");
        },
    });
}

//添加超链接
function aFormatter(value, row, index) {
    return [
        '<a href="/detail/' + value + '">' + value + '</a>'
    ].join("")
};

function convert_table_name(table_name) {
    var convert_list = {
        Herb: 'herb',
        Ingredient: 'ingredient',
        Prescription: 'prescription',
        Target: 'target',
        Disease: 'disease',
    }
    return convert_list[table_name]
}
