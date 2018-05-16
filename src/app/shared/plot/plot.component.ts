import { Component, OnInit, Input, OnChanges, ViewChild, ElementRef} from '@angular/core';

import * as d3 from 'd3';

@Component({
  selector: 'app-plot',
  templateUrl: './plot.component.html',
  styleUrls: ['./plot.component.css']
})
export class PlotComponent implements OnInit {

    @ViewChild('chart') chartContainer: ElementRef;
    @Input('width') containerWidth: number = 500;
    @Input('height') containerHeight: number = 300;
    @Input('xlabel') xlabel: string;
    @Input('ylabel') ylabel: string;
    public svg: any;
  
  constructor() { }
  
    ngOnChanges() {
        d3.select("svg").remove()
        this.draw()
    }

  ngOnInit() {
  }
  
    draw() {
    
        let margin: any = {top: 50, right: 50, bottom: 50, left: 70};
        // margin = {top: 20, right: 20, bottom: 50, left: 70}
        let width = this.containerWidth - margin.left - margin.right;
        let height = this.containerHeight - margin.top - margin.bottom;
        
        // The number of datapoints
        let n = 21;
        
        // 5. X scale will use the index of our data
        let xScale = d3.scaleLinear()
            .domain([0, n-1]) // input
            .range([0, width]); // output
            
        // 6. Y scale will use the randomly generate number 
        let yScale = d3.scaleLinear()
            .domain([0, 1]) // input 
            .range([height, 0]); // output
            
        // 7. d3's line generator
        let line = d3.line<{x: any, y: any}>()
            .x(function(d, i) { return xScale(i); }) // set the x values for the line generator
            .y(function(d) { return yScale(d.y); }) // set the y values for the line generator 
            .curve(d3.curveLinear); // apply smoothing to the line
            
        // 8. An array of objects of length N. Each object has key -> value pair, the key being "y" and the value is a random number
        let dataset = d3.range(n).map(function(d) { return {"y": d3.randomUniform(1)() } })
        
        this.svg = d3.select(this.chartContainer.nativeElement).append('svg')	      
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
            .append("g")
            .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
            
        // 3. Call the x axis in a group tag
        this.svg.append("g")
            .style("font", "inherit")
            .attr("stroke-width", 2)
            // .attr("class", "x axis")
            .attr("transform", "translate(0," + height + ")")
            .call(d3.axisBottom(xScale)); // Create an axis component with d3.axisBottom
            
        // text label for the x axis
        this.svg.append("text")
            .style("font", "inherit")
            .attr("transform", "translate(" + (width/2) + " ," + (height + margin.top) + ")")
            .style("text-anchor", "middle")
            .text(this.xlabel);
        
        // 4. Call the y axis in a group tag
        this.svg.append("g")
            .style("font", "inherit")
            .attr("stroke-width", 2)
            // .attr("class", "y axis")
            .call(d3.axisLeft(yScale)); // Create an axis component with d3.axisLeft
            
        // text label for the y axis
        this.svg.append("text")
            .style("font", "inherit")
            .attr("transform", "rotate(-90)")
            .attr("y", 0 - margin.left)
            .attr("x", 0 - (height / 2))
            .attr("dy", "1em")
            .style("text-anchor", "middle")
            .text(this.ylabel); 
        
        // 9. Append the path, bind the data, and call the line generator 
        this.svg.append("path")
            .datum(dataset) // 10. Binds data to the line 
            .attr("fill", "none")
            .attr("stroke", "#ffab00")
            .attr("stroke-width",3)
            .attr("d", line); // 11. Calls the line generator 
            
        // 12. Appends a circle for each datapoint 
        this.svg.selectAll(".dot")
            .data(dataset)
            .enter()
            .append("circle") // Uses the enter().append() method
            .attr("fill", "#ffab00")
            .attr("stroke", "#fff")
            .attr("cx", function(d, i) { return xScale(i) })
            .attr("cy", function(d) { return yScale(d.y) })
            .attr("r", 5);
    
    }
  
    ngAfterContentInit() {
        // this.draw()
    }

}
