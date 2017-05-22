var quadratic = function () {
	
	var PADDING = 2;	/* frame around entire layout */
	var SPACING = 2; /* minimum space between boxes */
	var wsizer = undefined, hsizer = undefined, xmax = 0, ymax = 0;
	
	function quadratic(data) {
		var wrappers = [];
		var numh = Math.ceil(Math.sqrt(data.length))
		var xp = PADDING, yp = PADDING;
		for (var i = 0; i < data.length; i++) {
			var wrapper = { x: xp, y: yp, item: data[i] };
			xp += wsizer(data[i]) + SPACING
			xmax = Math.max(xmax, xp)
			ymax = Math.max(ymax, yp + hsizer(data[i]))
			if((i + 1) % numh == 0) {
				xp = PADDING
				yp = ymax + SPACING
			}
			wrappers.push(wrapper);
		}
		return wrappers;
	}
	
	quadratic.width = function(x) {
    if (!arguments.length) return wsizer;
    wsizer = x;
    return quadratic;
	}

	quadratic.height = function(x) {
    if (!arguments.length) return hsizer;
    hsizer = x;
    return quadratic;
	}
	
	quadratic.xmax = function(x) {
		return xmax + PADDING;
	}

	quadratic.ymax = function(x) {
		return ymax + PADDING;
	}

	return quadratic;
}


PMV.hotspot = function(data, at) {

	data.shuffle().sort(function(da, db) { return PMV.getv(da, at.sort) - PMV.getv(db, at.sort) } )
  
	var wmax = d3.max(data, function(d) { return PMV.getv(d, at.width) });
	var hmax = d3.max(data, function(d) { return PMV.getv(d, at.height) });
	
	if(at.width.match("^NO") && at.height.match("^NO")) {
		// magic proportional mode: if both are "number of" they'll get the same scale
		wmax = hmax = Math.max(wmax, hmax);
	} 
  
	var wscale = d3.scale.linear()
    .domain([0, wmax])
    .rangeRound([4, 40]);

  var hscale = d3.scale.linear()
    .domain([0, hmax])
    .rangeRound([4, 40]);
  
	var fscale = d3.scale.linear()
    .domain([0, d3.max(data, function(d) { return PMV.getv(d, at.shade) })])
    .range([100, 0]);

	var layout = quadratic()
		.width(function(d) { return wscale(PMV.getv(d, at.width)) })
		.height(function(d) { return hscale(PMV.getv(d, at.height)) });
		 
	var items = layout(data);
	
	d3.selectAll("svg").remove();
	var chart = d3.select("#chart-wrapper").append("svg")
    .attr("class", "chart")
    .attr("width", layout.xmax())
    .attr("height", layout.ymax());

  chart.selectAll("rect")
    .data(items)
    .enter().append("rect")
    .attr("x", function(d) { return d.x })
    .attr("y", function(d) { return d.y })
    .attr("width", function(d) { return wscale(PMV.getv(d.item, at.width)) })
    .attr("height", function(d) { return hscale(PMV.getv(d.item, at.height)) })
		.attr("shape-rendering", "crispEdges")
    .style("fill", function(d) { return "hsl(200, 80%, " + fscale(PMV.getv(d.item, at.shade)) + "%)" })
		.call(tooltip(function(d) { return d.item }));
}

