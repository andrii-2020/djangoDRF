import { Component, OnInit } from '@angular/core';
import {IOffices} from '../../interfaces/offices';
import {OfficeService} from '../../services/office-service';
import {FormControl, FormGroup} from '@angular/forms';
import {EmployeesService} from '../../services/employees.service';
import {IEmployees} from '../../interfaces/employees';


@Component({
  selector: 'app-offices',
  templateUrl: './offices.component.html',
  styleUrls: ['./offices.component.css']
})
export class OfficesComponent implements OnInit {
  offices: IOffices[];
  employees: IEmployees[];
  form: FormGroup;
  visibleForm = false;
  user = false;
  constructor(private officeService: OfficeService) {
  }


  ngOnInit(): void {
    this.officeService.getAll().subscribe(val => this.offices = val );
    this.officeService.getEmployees().subscribe(val => this.employees = val);
    this.form = new FormGroup({
      name: new FormControl(''),
      city: new FormControl(''),
    });
  }

  save(form: FormGroup): void {
    this.officeService.create(form.getRawValue()).subscribe(() => this.ngOnInit() );
  }

  showform(): void {
    this.visibleForm = !this.visibleForm;
  }

  delete(id: number): void {
    this.officeService.delete(id).subscribe(() => this.ngOnInit());
  }

  showYser(): void {
    this.user = !this.user;
  }

}
