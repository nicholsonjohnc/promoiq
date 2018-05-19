import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { TabComponent } from './shared/tab/tab.component';
import { TabsComponent } from './shared/tabs/tabs.component';
import { PlotComponent } from './shared/plot/plot.component';
import { DemandComponent } from './dashboard/demand/demand.component';
import { SelectorComponent } from './dashboard/selector/selector.component';
import { Ng2FileInputModule } from 'ng2-file-input';
import { HttpClientModule } from '@angular/common/http';
import { UploaderService } from './service/uploader/uploader.service';

@NgModule({
  declarations: [
    AppComponent,
    TabComponent,
    TabsComponent,
    PlotComponent,
    DemandComponent,
    SelectorComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    Ng2FileInputModule.forRoot()
  ],
  providers: [
    UploaderService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
