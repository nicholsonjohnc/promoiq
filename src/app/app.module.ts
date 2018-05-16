import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { TabComponent } from './shared/tab/tab.component';
import { TabsComponent } from './shared/tabs/tabs.component';
import { PlotComponent } from './shared/plot/plot.component';
import { DemandComponent } from './dashboard/demand/demand.component';

@NgModule({
  declarations: [
    AppComponent,
    TabComponent,
    TabsComponent,
    PlotComponent,
    DemandComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
