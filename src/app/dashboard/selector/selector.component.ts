import { Component, OnInit } from '@angular/core';
import { Ng2FileInputAction } from 'ng2-file-input';
import { UploaderService } from '../../service/uploader/uploader.service';

@Component({
  selector: 'app-selector',
  templateUrl: './selector.component.html',
  styleUrls: ['./selector.component.css']
})
export class SelectorComponent implements OnInit {

  constructor(private uploaderService: UploaderService) { }

  ngOnInit() {
  }
  
  onAction(event) {
    if(event.action===Ng2FileInputAction.Added) {
      console.log(event)
    }
  }

}
