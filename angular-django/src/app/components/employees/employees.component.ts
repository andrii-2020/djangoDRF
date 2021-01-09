import {Component, Input, OnInit} from '@angular/core';
import {IEmployees} from '../../interfaces/employees';
import {OfficeService} from '../../services/office-service';

@Component({
  selector: 'app-employees',
  templateUrl: './employees.component.html',
  styleUrls: ['./employees.component.css']
})
export class EmployeesComponent implements OnInit {

  @Input()
  user: IEmployees;
  constructor(private officeService: OfficeService) {
  }

  ngOnInit(): void {
    console.log(this.user);
  }

   deleteEmp(id: number): void {
     this.officeService.deleteEmployees(id).subscribe(() => this.ngOnInit());
  }
}
