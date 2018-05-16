import { Component, OnInit, Input } from '@angular/core';
import { TabsComponent as Tabs } from '../tabs/tabs.component';

@Component({
  selector: 'app-tab',
  templateUrl: './tab.component.html',
  styleUrls: ['./tab.component.css']
})
export class TabComponent implements OnInit {

  @Input('tab-title') tabTitle: string;
  public active: boolean;
  public activeClass: string;

  constructor(tabs: Tabs) {

    tabs.addTab(this);

  }

  ngOnInit() {
  }

}