import { Component, OnInit, ViewChild, ElementRef, HostListener } from '@angular/core';

@Component({
  selector: 'app-demand',
  templateUrl: './demand.component.html',
  styleUrls: ['./demand.component.css']
})
export class DemandComponent implements OnInit {

  @ViewChild('container') container: ElementRef;
  public containerWidth: number;
  public containerHeight: number;
  public xLabel: any;
  public yLabel: any;
  
  constructor() {
  }

  ngOnInit() {
     this.xLabel = 'Date';
     this.yLabel = 'Sales';
  }
  
  @HostListener('window:resize', ['$event'])
  onResize(event){
     this.containerWidth = this.container.nativeElement.offsetWidth;
     this.containerHeight = this.container.nativeElement.offsetWidth / 1.618;
  }
  
  ngAfterContentInit() {
     this.containerWidth = this.container.nativeElement.offsetWidth;
     this.containerHeight = this.container.nativeElement.offsetWidth / 1.618;

  }

}
