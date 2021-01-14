import {Component, OnInit} from '@angular/core';
import {IEmployees} from '../../interfaces/employees';
import {OfficeService} from '../../services/office-service';
import {FormControl, FormGroup} from '@angular/forms';

@Component({
  selector: 'app-employees',
  templateUrl: './employees.component.html',
  styleUrls: ['./employees.component.css']
})
export class EmployeesComponent implements OnInit {
  visibleFor = false;
  formE: FormGroup;
  id = new FormControl('');
  constructor() {
  }

  ngOnInit(): void {
    this.formE = new FormGroup({
      name: new FormControl(''),
      age: new FormControl(''),
      city: new FormControl(''),
      id: this.id
    });
  }

  editEmployee(id: any, formE: FormGroup): void {
    console.log(id, formE.getRawValue());
    this.visibleFor = !this.visibleFor;
  }
}
