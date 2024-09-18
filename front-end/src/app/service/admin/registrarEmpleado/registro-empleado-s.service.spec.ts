import { TestBed } from '@angular/core/testing';

import { RegistroEmpleadoSService } from './registro-empleado-s.service';

describe('RegistroEmpleadoSService', () => {
  let service: RegistroEmpleadoSService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(RegistroEmpleadoSService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
