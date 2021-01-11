import { Component, OnInit } from '@angular/core';
import {IOffices} from '../../interfaces/offices';
import {OfficeService} from '../../services/office-service';
import {FormControl, FormGroup} from '@angular/forms';
import {IEmployees} from '../../interfaces/employees';

@Component({
  selector: 'app-offices',
  templateUrl: './offices.component.html',
  styleUrls: ['./offices.component.css']
})
export class OfficesComponent implements OnInit {
  offices: IOffices[];
  form: FormGroup;
  visibleForm = false;
  visibleFor = false;
  constructor(private officeService: OfficeService) {
  }


  ngOnInit(): void {
    this.officeService.getAll().subscribe(val => {
      this.offices = val;
    } );
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
  showformE(): void {
    this.visibleFor = !this.visibleFor;
  }
}
