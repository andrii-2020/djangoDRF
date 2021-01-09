import { Component, OnInit } from '@angular/core';
import {OfficeService} from '../services/office-service';
import {IOffices} from '../interfaces/offices';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  ngOnInit(): void {
  }

}
