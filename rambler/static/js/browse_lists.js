$(function () {
    initTable();
});

$(document).ready(function(){
    $('#browse_type').change(function(){
    　　change_option();
    })
});

var change_option_flag = true;

function initTable(){
    $('#table').bootstrapTable({
        height: "auto",
        toolbar: '#toolbar',
        method: 'post',
        contentType: "application/x-www-form-urlencoded",
        url:"/browse_ajax",
        pageNumber: 1,
        pagination:true,
        queryParams:queryParams,
        sidePagination:'server',
        pageSize:15,
        pageList:[15,25,50],
        responseHandler:responseHandler,
        columns :[]
    })

    //请求服务数据时所传参数
    function queryParams(params){
        var browse_type = $("#browse_type").val();
        return {
            page_size : params.limit, //每一页的数据行数，默认是上面设置的10(pageSize)
            page_num : params.offset/params.limit+1, //当前页面,默认是上面设置的1(pageNumber)
            table_name : browse_type
        }
    };

    //请求成功方法
    function responseHandler(result){
        if (change_option_flag){
            change_option_flag = false;
            result.columns[0].formatter = aFormatter
            $('#table').bootstrapTable("refreshOptions", {columns: result.columns});
            }
        return {
            total : result.Total,
            rows : result.Data
        };
    };

    //添加超链接
    function aFormatter(value, row, index) {
        return [
            '<a href="/detail/'+value+'">'+value+'</a>'
                ].join("")
    };


}


function change_option(){
    change_option_flag = true;
    $('#table').bootstrapTable("refreshOptions", {columns: []});
};