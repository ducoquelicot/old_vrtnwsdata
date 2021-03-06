var choose = choices => { 
    var index = Math.floor(Math.random() * choices.length);
    return choices[index];
}

var race = ['White', 'Black'],
    guilty = ['True', 'False'];

var persons = d3.range(100).map( d => {return {race: choose(race), guilty: choose(guilty)}});

console.log(persons);

var margin = {top: 30, right: 30, bottom: 30, left: 30},
width = 500 - margin.left - margin.right,
height = 500 - margin.top - margin.bottom;

var svg = d3.select('#simulation')
    .append('svg')
        .attr('viewBox', '0 0 500 500')
        .attr('preverseAspectRatio', 'xMidYMid')
    .append('g')
        .attr('id', 'content')
        .attr("transform", "translate(" + margin.left + ',' + margin.top + ")");


var data = []
for (var i=0; i<10; i++) {
    person = choose(persons);
    data.push(person);

    var u = svg
        .selectAll("circle")
        .data(data);

    u = u
        .enter().append("circle")
        .attr('r', 5)
        .merge(u);

    u.transition()
        .duration(1000)
        .attr('cx', (d, i) => i * 12)
}

console.log(data);
