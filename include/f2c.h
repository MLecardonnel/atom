/* f2c.h  --  Standard Fortran to C header file */

/**  barf  [ba:rf]  2.  "He suggested using FORTRAN, and everybody barfed."

	- From The Shogakukan DICTIONARY OF NEW ENGLISH (Second edition) */

#ifndef F2C_INCLUDE
#define F2C_INCLUDE

typedef long int integer;
typedef char *address;
typedef short int shortint;
typedef float real;
typedef double doublereal;
typedef struct {
    real r, i;
} complex;
typedef struct {
    doublereal r, i;
} doublecomplex;
typedef long int logical;
typedef short int shortlogical;

#define TRUE_ (1)
#define FALSE_ (0)

/* Extern is for use with -E */
#ifndef Extern
#define Extern extern
#endif

/* I/O stuff */

#ifdef f2c_i2
/* for -i2 */
typedef short flag;
typedef short ftnlen;
typedef short ftnint;
#else
typedef long flag;
typedef long ftnlen;
typedef long ftnint;
#endif

#define VOID void

typedef long Long;

/* procedure parameter types for -A and -C++ */

#ifdef __cplusplus
typedef int /* Unknown procedure type */ (*U_fp)(...);
typedef shortint (*J_fp)(...);
typedef integer (*I_fp)(...);
typedef real (*R_fp)(...);
typedef doublereal (*D_fp)(...), (*E_fp)(...);
typedef /* Complex */ VOID (*C_fp)(...);
typedef /* Double Complex */ VOID (*Z_fp)(...);
typedef logical (*L_fp)(...);
typedef shortlogical (*K_fp)(...);
typedef /* Character */ VOID (*H_fp)(...);
typedef /* Subroutine */ int (*S_fp)(...);
#else

typedef int /* Unknown procedure type */ (*U_fp)();

typedef shortint (*J_fp)();

typedef integer (*I_fp)();

typedef real (*R_fp)();

typedef doublereal (*D_fp)(), (*E_fp)();

typedef /* Complex */ VOID (*C_fp)();

typedef /* Double Complex */ VOID (*Z_fp)();

typedef logical (*L_fp)();

typedef shortlogical (*K_fp)();

typedef /* Character */ VOID (*H_fp)();

typedef /* Subroutine */ int (*S_fp)();

#endif
/* E_fp is for real functions when -R is not specified */
typedef VOID C_f;    /* complex function */
typedef VOID H_f;    /* character function */
typedef VOID Z_f;    /* double complex function */
typedef doublereal E_f;    /* real function with -R not specified */

/* undef any lower-case symbols that your C compiler predefines, e.g.: */

#ifndef Skip_f2c_Undefs
#undef cray
#undef gcos
#undef mc68010
#undef mc68020
#undef mips
#undef pdp11
#undef sgi
#undef sparc
#undef sun
#undef sun2
#undef sun3
#undef sun4
#undef u370
#undef u3b
#undef u3b2
#undef u3b5
#undef unix
#undef vax
#endif
#endif
