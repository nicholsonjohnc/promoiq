import { Component, OnInit, Input } from '@angular/core';
import { TabComponent as Tab } from '../tab/tab.component';

@Component({
  selector: 'app-tabs',
  templateUrl: './tabs.component.html',
  styleUrls: ['./tabs.component.css']
})
export class TabsComponent implements OnInit {

  @Input('tabs-layout') tabsLayout: 'standard' | 'flex';
  public tabs: Tab[] = [];

  constructor() { }

  ngOnInit() {
  }

  selectTab($event: any, tab: Tab) {

    $event.preventDefault();
    this.tabs.forEach((tab) => {
      tab.active = false;
      tab.activeClass = '';
    });
    tab.active = true;
    tab.activeClass = 'active';

  }

  addTab(tab: Tab) {

    if (this.tabs.length === 0) {
      tab.active = true;
      tab.activeClass = 'active';
    }
    this.tabs.push(tab);

  }

}
