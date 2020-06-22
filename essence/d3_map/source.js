

function draw(topo) {
    console.log('Draw', topo);
    const geojson = topojson.feature(topo, topo.objects.district);

    var projection = d3.geoMercator().fitSize([1000, 1000], geojson);
    var geoGenerator = d3.geoPath()
        .projection(projection);
    var u = d3.select('#content g.map')
        .selectAll('path')
        .data(geojson.features);
    u.enter()
        .append('path')
        .attr('d', geoGenerator);

}

d3.json("./district_fokjouantwerpen.json").then(function (geojson) {
    draw(geojson)
})

// draw(input)