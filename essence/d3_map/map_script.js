var svg = d3.select('#map')
    .append('svg')
        .attr('viewBox', '0 0 2000 2000')
        .attr('preserveAspectRatio', 'xMidYMid')

d3.json("topo.json")
    .then( function(data) {
        console.log('Draw', data)
        const geojson = topojson.feature(data, data.objects.district);
        var projection = d3.geoMercator().fitSize([1000, 1000], geojson);
        
        svg.append('g')
            .selectAll('path')
            .data(geojson.features)
            .enter()
            .append('path')
            .attr("d", d3.geoPath().projection(projection))
            .style('fill', '#69b3a2')
            .style('stroke', '#FFFFFF')

    });

d3.json("https://ext-api-gw-p.antwerpen.be/digipolis/bigbellywaste/v1/entities?apikey=95cc3eb9-ff40-455c-9223-d5998af806c9&limit=1000")
    .then( function(data) {

        var projection = d3.geoMercator().fitSize([1000, 1000], data);

        console.log(data);

        data.forEach(function(d) {
            console.log(d.location.value)
        });

        svg.append('g')
            .selectAll('circle')
            .data(data)
            .enter()
            .append('circle')
            .attr('cx', d => projection(d.location.value.coordinates[0]))
            .attr('cy', d => projection(d.location.value.coordinates[1]))
            .attr('r', 5)
            .style('fill', 'black')
    });